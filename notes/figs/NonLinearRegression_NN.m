clear;close all
a1_data=2;
a2_data=2.5;
% noise=1;
x=[-0.5:0.1:2.5];
% Fun=@(x,a1,a2) a1*(x+a2).^2;
% Fun=@(x,a1,a2) a1-a2+a1*cos(a1*x.^2);
% Fun=@(x,a1,a2) x.^3/(a2+1)+x.^2/(a1+3)+(a2)*x+a2^2+a1*a2*cos(a1*a2*x);
Fun=@(x,a1,a2) tanh(a1*x-a2);
y_data=sign(Fun(x,a1_data,a2_data));%+noise*randn(size(x));
y_fit=Fun(x,a1_data,a2_data);
r_fit=y_fit-y_data;
S_fit=sum(r_fit.^2);
x_range=[-1:0.1:3];

S_fun = @(a1,a2) sum((y_data-Fun(x,a1,a2)).^2);

da1=0.01;
da2=0.01;
dS_da1=@(x,y,a1,a2,da1) (S_fun(a1+da1,a2)-S_fun(a1,a2))/da1;
dS_da2=@(x,y,a1,a2,da2) (S_fun(a1,a2+da2)-S_fun(a1,a2))/da2;



a1_0=a1_data;
a2_0=a2_data;
J_0=[dS_da1(x,y_data,a1_0,a2_0,da1),dS_da2(x,y_data,a1_0,a2_0,da2)];

a1_3=1.6;
a2_3=1.1;
a1_2=-.2;
a2_2=.65;
a1_1=.7;
a2_1=.8;

J_1=[dS_da1(x,y_data,a1_1,a2_1,da1),dS_da2(x,y_data,a1_1,a2_1,da2)];
J_2=[dS_da1(x,y_data,a1_2,a2_2,da1),dS_da2(x,y_data,a1_2,a2_2,da2)];
J_3=[dS_da1(x,y_data,a1_3,a2_3,da1),dS_da2(x,y_data,a1_3,a2_3,da2)];



%% Plotting
Fig=figure(...
    'Units','normalized',...
    'Position',[.33 .5 .63 .4],...
    'Color',[1 1 1],...%    'renderer','painters',...
    'WindowStyle','normal',...
    'PaperPositionMode','auto',...
    'PaperOrientation','landscape');
subplot(1,2,1);
hold on
h=plot(x,y_data,'x','markersize',8,'linewidth',2,'color',[0,0,0]);
for i=1:length(x)
    plot([x(i) x(i)], [y_data(i) Fun(x(i),a1_data,a2_data)],'k')
    % plot([x(i) x(i)], [y_data(i) a1_1*x(i)+a2_1],'r')
end
plot(x_range,Fun(x_range,a1_0,a2_0),'k:','linewidth',2);
plot(x_range,Fun(x_range,a1_1,a2_1),'r:','linewidth',2);
plot(x_range,Fun(x_range,a1_2,a2_2),'g:','linewidth',2);
plot(x_range,Fun(x_range,a1_3,a2_3),'b:','linewidth',2);
xlim([x_range(1),x_range(end)])
% ylim([0,1])
hold off
set(gca,'TickLabelInterpreter','latex',...
    'LineWidth',1.2,...
    'FontSize',16);
xlabel('$x$','Interpreter','latex');
ylabel('$f(x)$','Interpreter','latex');
axis square
box
leg=legend('Data','Residuals', 'location','northwest');
set(leg,'interpreter','latex')

subplot(1,2,2);
a1s=-1:0.1:3;
a2s=0.1:0.1:2;
[M,C]=meshgrid(a1s,a2s);
axis square
for j=1:length(a1s)
    for i=1:length(a2s)
        S(i,j)=S_fun(M(i,j),C(i,j));
    end
end
contourf(M,C,log(S),10)
colormap(flipud(pink));%flipud
xlabel('$a1$','Interpreter','latex');
ylabel('$a2$','Interpreter','latex');
set(gca,'TickLabelInterpreter','latex',...
    'LineWidth',1.2,...
    'FontSize',16)
hold on
arrowscale=1/200;
plot(a1_0,a2_0,'*','markersize',12,'linewidth',2,'color',[0,0,0]);
plot(a1_1,a2_1,'*','markersize',12,'linewidth',2,'color',[1,0,0]);
quiver(a1_1,a2_1,-J_1(1)*arrowscale,-J_1(2)*arrowscale,...
    'markersize',12,'linewidth',2,'color',[1,0,0],'MaxHeadSize',.9);
plot(a1_2,a2_2,'*','markersize',12,'linewidth',2,'color',[0,1,0]);
quiver(a1_2,a2_2,-J_2(1)*arrowscale,-J_2(2)*arrowscale,...
    'markersize',12,'linewidth',2,'color',[0,1,0],'MaxHeadSize',.7);
plot(a1_3,a2_3,'*','markersize',12,'linewidth',2,'color',[0,0,1]);
quiver(a1_3,a2_3,-J_3(1)*arrowscale,-J_3(2)*arrowscale,...
    'markersize',12,'linewidth',2,'color',[0,0,1],'MaxHeadSize',2);
hold off
xlim([a1s(1),a1s(end)]);
ylim([a2s(1),a2s(end)]);

colo=colorbar;
set(colo,'FontSize',16, 'TickLabelInterpreter','latex')
ylabel(colo,'log($S$)','Interpreter','latex')